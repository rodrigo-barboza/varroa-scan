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
                            v-for="(input, index) in ((files.length >= 5) ? 5 : files.length + 1)"
                            :key="index"
                            v-model="file[index]"
                            :text-message="`Carregar imagem ${index + 1}`"
                            allowed-extensions="jpg,png,jpeg"
                            size="sm"
                            @update:model-value="handleFileUpload($event, index)"
                            @remove="handleFileRemove(index)"
                        />
                    </div>
                </div>
                <div class="new-analisys__actions">
                    <button
                        class="new-analisys__secondary-button"
                        @click="handleBackRouter"
                    >
                        <
                    </button>
                    <button class="new-analisys__button">
                        Analisar
                    </button>
                </div>
            </div>
        </ion-content>
    </ion-page>
</template>

<script setup>
import { ref } from 'vue';
import { toastController } from '@ionic/vue';
import AppTitle from '../components/Layout/AppTitle.vue';
import NumberInput from '../components/NumberInput.vue';
import FileUpload from '../components/FileUpload.vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const numberOfBees = ref(0);
const file = ref([]);
const files = ref([]);

const presentToast = async (message) => {
    const toast = await toastController.create({
        message,
        duration: 15000,
        position: 'top',
        cssClass: 'custom-toast',
        color: 'danger',
    });

    await toast.present();
};

const handleFileUpload = (uploadedFile, index) => {
    if (files.value.length >= 5) {
        presentToast('Limite de arquivos atingido');        
        return;
    }

    if (files.value.findIndex((f) => f?.name === uploadedFile?.name) !== -1) {
        presentToast('Arquivo duplicado, escolha outro');
        file.value[index] = null;
        return;
    }

    if (index >= files.value.length) {
        files.value.push(uploadedFile);
    } else {
        files.value[index] = uploadedFile;
    }

    files.value = file.value = files.value.filter((f) => f !== null);
};

const handleBackRouter = () => {
    files.value = file.value = [];
    router.back();
}
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
