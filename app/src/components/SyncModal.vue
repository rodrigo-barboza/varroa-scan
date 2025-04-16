<template>
    <div>
        <ion-backdrop></ion-backdrop>
        <div class="modal">
            <div class="modal__content">
                <ion-item-divider>
                    Analise em andamento
                </ion-item-divider>
                <div class="modal__text">
                    <ion-spinner name="circular"></ion-spinner>
                    <div>Analisando...</div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { IonSpinner, IonBackdrop, IonItemDivider } from '@ionic/vue';

</script>

<style lang="scss" scoped>

ion-item-divider {
    font-size: 18px;
    line-height: 27px;
    color: #333333;
    padding-bottom: 16px;
}

ion-spinner {
    --color: #539C7C;
    width: 48px;
    height: 48px;
}

ion-backdrop {
    opacity: 0.5;
    background: #000;
}

.modal {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translateY(-50%) translateX(-50%);
    z-index: 100;
    background: var(--ion-background-color, #fff);
    width: 90%;
    border-radius: 10px;
    padding: 16px;
    font-weight: 500;

    &__content {
        display: flex;
        flex-direction: column;
        height: 100%;
        gap: 12px;
    }

    &__text {
        display: flex;
        gap: 16px;
        font-size: 16px;
        line-height: 24px;
        align-items: center;
        color: #3A3A3A;
    }
}


</style>
