<template>
    <div>
        <div
            v-if="withMenu"
            style="display: flex; justify-content: space-between; margin-bottom: 20px;"
        >
            <div><img :src="MenuIcon" @click="showAboutModal = true" /></div>
            <div style="margin-left: -15px"><img :src="AppLogo" width="100%" /></div>
            <div></div>
        </div>
        <div class="app-title">
            <div>
                <div class="app-title__title">
                    {{ title }}
                </div>
                <div class="app-title__subtitle">
                    {{  subtitle }}
                </div>
            </div>
            <div
                v-if="withSyncButton"
                ref="syncButton"
                class="app-title__sync-button"
                @click="$emit('on-sync-click')"
            >
                <ion-icon :icon="syncOutline"></ion-icon>
                <div class="app-title__sync-badge">
                    {{ unsincronizedTasksCount ?? 0 }}
                </div>
            </div>
            <div
                v-if="showAboutModal"
                class="app-sidesheet-overlay"
                @click="showAboutModal = false"
            >
                <div class="app-sidesheet">
                    <div class="app-sidesheet__title">
                        Sobre o aplicativo
                    </div>
                    <p class="app-sidesheet__description">
                        Este aplicativo foi desenvolvido como parte do Trabalho de Conclusão de Curso (TCC) do aluno Rodrigo Leandro Ramos Barboza da Silva, no curso de Engenharia de Computação da Universidade Federal do Vale do São Francisco (UNIVASF), Campus Juazeiro.
                        <br><br>
                        O objetivo do projeto é oferecer uma ferramenta móvel para análise de infestações do ácaro Varroa destructor em colônias de abelhas, utilizando tecnologias de visão computacional e redes neurais convolucionais. O aplicativo permite ao usuário capturar imagens, realizar análises automáticas, salvar os resultados e consultar o histórico de análises, contribuindo para o monitoramento da saúde das abelhas.
                        <br><br>
                        Orientador: Prof. Dr. Brauliro Gonçalves Leal<br>
                        Coorientadora: Profa. Dra. Eva Monica Sarmento da Silva
                        <br><br>
                        Ano de Desenvolvimento: 2024-2025
                    </p>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { IonIcon } from '@ionic/vue';
import { syncOutline } from 'ionicons/icons';
import { computed, ref } from 'vue';
// import { useTaskStore } from '../../store/taskStore';
import MenuIcon from '../../theme/images/menu.svg';
import AppLogo from '../../theme/images/app-logo-inline.svg';

defineProps({
    title: {
        type: String,
        required: true,
        default: 'App Title',
    },
    subtitle: {
        type: String,
        default: '',
    },

    withSyncButton: {
        type: Boolean,
        default: false,
    },

    withMenu: {
        type: Boolean,
        default: false,
    },
});

// const store = useTaskStore();

const showAboutModal = ref(false);

// const unsincronizedTasksCount = computed(() => store.taskCount);
const modalVisibility = computed(() => showAboutModal.value ? '0' : '-100%');

</script>

<style lang="scss" scoped>

ion-icon {
    font-size: 20px;
}
.app-sidesheet-overlay {
    transition: all 0.3s ease-in-out;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.2);
    z-index: 999;
}

.app-sidesheet {
    transition: all 0.3s ease-in-out;
    width: 85%;
    background: #fff;
    height: 100%;
    position: fixed;
    top: 0;
    left: 0;
    z-index: 1000;
    padding: 28px;
    margin-left: v-bind(modalVisibility);

    &__title {
        font-size: 20px;
        font-weight: 600;
        line-height: 33.6px;
        color: #333333;
        margin-bottom: 9px;
    }

    &__description {
        margin-top: 15px;
        font-size: 13px;
        font-weight: 400;
        line-height: 21.44px;
        text-align: left;
        color: #7A7A7A;
        text-align: justify;
    }
}

.app-title {
    display: flex;
    justify-content: space-between;

    &__title {
        font-size: 24px;
        font-weight: 600;
        line-height: 33.6px;
        color: #333333;
        margin-bottom: 9px;
    }

    &__subtitle {
        font-size: 16px;
        font-weight: 400;
        line-height: 21.44px;
        text-align: left;
        color: #7A7A7A;
    }

    &__sync-button {
        width: 46.03px;
        height: 44.5px;
        padding: 14px;
        padding-left: 12px;
        padding-top: 12px;
        background: #F5F5F5;
        gap: 4px;
        border-radius: 12px;
        border: 1px solid #EFEFEF;
        position: relative;

        &:hover {
            cursor: pointer;
            background: #F8F8F8;
        }
    }

    &__sync-badge {
        width: 25px;
        height: 25px;
        padding: 5px;
        padding-top: 2px;
        padding-left: 7px;
        background: #C95632;
        border-radius: 50%;
        position: absolute;
        bottom: 0;
        margin-bottom: -6px;
        right: 0;
        margin-right: -3px;
        border: 1px solid #EFEFEF;
        color: #fff;
        font-size: 14px;
        font-weight: 600;
    }
}

</style>
