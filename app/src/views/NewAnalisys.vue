<template>
    <ion-page>
		<ion-content>
            <div class="new-analisys-view">
                <div class="view-container">
                    <app-title
                        title="Nova análise"
                        subtitle="Carregue até 5 imagens para fazer a análise de infestação"
                    />
                    <div style="display: flex; flex-direction: column; gap: 16px">
                        <number-input
                            v-model="numberOfBees"
                            label="Estimativa da quantidade de abelhas"
                        />
                        <file-upload
                            v-for="(item, index) in files"
                            :key="index"
                            :item="item"
                            @remove-file="handleRemoveFile(index)"
                        />
                        <file-upload
                            v-if="files.length < 5"
                            text-message="Carregar imagem"
                            @click.prevent="takePicture()"
                        />
                    </div>
                </div>
                <div class="new-analisys__actions">
                    <button
                        class="new-analisys__secondary-button"
                        @click="handleBackRouter"
                    >
                        <img :src="ArrowLeft">
                    </button>
                    <button
                        class="new-analisys__button"
                        @click="handleSubmitForm"
                    >
                        Analisar
                    </button>
                </div>
            </div>
            <sync-modal v-if="showAnalyzingModal" />
        </ion-content>
    </ion-page>
</template>

<script setup>
import { Camera, CameraResultType } from '@capacitor/camera';
import { onIonViewDidEnter, toastController } from '@ionic/vue';
import { ref } from 'vue';
import { useAnalysisStore } from '../store/analysesStore';
import { useRouter } from 'vue-router';
import AnalysisController from '../server/controllers/AnalysisController';
import AppTitle from '../components/Layout/AppTitle.vue';
import ArrowLeft from '../theme/images/arrow-left.png';
import FileUpload from '../components/FileUpload.vue';
import NumberInput from '../components/NumberInput.vue';
import SyncModal from '../components/SyncModal.vue';

const router = useRouter();
const store = useAnalysisStore();
const numberOfBees = ref(0);
const file = ref(null);
const files = ref([]);
const showAnalyzingModal = ref(false);

const presentToast = async (message) => {
    const toast = await toastController.create({
        message,
        duration: 3000,
        position: 'top',
        cssClass: 'custom-toast',
        color: 'danger',
        buttons: [
            {
                text: 'Fechar',
                role: 'cancel',
            },
        ]
    });

    await toast.present();
};

const resetForm = () => {
    files.value = file.value = [];
    numberOfBees.value = 0;
};

const handleBackRouter = () => (resetForm(), router.back());
const handleAddFile = (newFile) => files.value.push(newFile);
const handleRemoveFile = (index) => files.value.splice(index, 1);

const makeFile = async (webPath) => {
    const response = await fetch(webPath);
    const blob = await response.blob();
    return new File([blob], `${Date.now()}.${blob.type.split('/').pop()}`, {
        type: blob.type,
    });
};

const takePicture = async () => {
    try {
        const { webPath } = await Camera.getPhoto({
            quality: 90,
            allowEditing: false,
            resultType: CameraResultType.Uri,
            saveToGallery: true,
        });

        handleAddFile(await makeFile(webPath));
    } catch (error) {
        console.error('Erro ao abrir a câmera:', error);
    }
};

const validatedForm = () => {
    if (numberOfBees.value <= 0) {
        presentToast('O número de abelhas deve ser maior que zero');
        return false;
    }

    if (!numberOfBees.value) {
        presentToast('Preencha a quantidade de abelhas');
        return false;
    }

    if (files.value.length === 0) {
        presentToast('Selecione ao menos uma imagem');
        return false;
    }

    return true;
}

const makeFormData = () => {
    const form = new FormData();

    form.append('bee_count_estimate', numberOfBees.value);
    files.value.forEach((image) => form.append('images', image));

    return form;
};

const handleSubmitForm = async () => {
    if (validatedForm()) {
        showAnalyzingModal.value = true;

        try {
            const response = await (new AnalysisController()).store(makeFormData());
            store.setCurrentAnalysis(await response.json());
            router.push({ name: 'analysis.result' });
        } catch (error) {
            presentToast('Erro ao fazer análise');
            console.error(error);
        } finally {
            showAnalyzingModal.value = false;
        }
    }
};

onIonViewDidEnter(() => {
    resetForm();
});

</script>

<style lang="scss" scoped>
.new-analisys-view {
    position: relative;
}

:root {
    --ion-color-danger: #0f0;
    --ion-color-danger-rgb: 201, 44, 63;
    --ion-color-danger-contrast: #ffffff;
    --ion-color-danger-contrast-rgb: 255, 255, 255;
    --ion-color-danger-shade: #0f0;
    --ion-color-danger-tint: #0f0;
}

.new-analisys {
    &__actions {
        position: fixed;
        bottom: 0;
        padding: 0px 20px;
        display: flex;
        gap: 8px;
        width: 100%; 
        margin-bottom: 20px;
    }

    &__button {
        width: 100%;
        padding: 12px 20px;
        gap: 4px;
        border-radius: 8px;
        border: 1px solid #FFA41B;
        background: #FFA41B;
        color: #5C4016;
        font-weight: 600;
        font-size: 14px;
        line-height: 21px;

        &:hover {
            cursor: pointer;
            background: rgb(255, 239, 205)
        }
    }

    &__secondary-button {
        width: 46px;
        height: 46px;
        padding: 12px;
        padding-left: 16px;
        padding-top: 10px;
        border-radius: 8px;
        border: 1px solid #5C4016;
        background: white;
        color: #5C4016;
        font-weight: 500;
        font-size: 24px;
        line-height: 21px;

        &:hover {
            cursor: pointer;
            background: rgb(255, 239, 205)
        }
    }
}
</style>
