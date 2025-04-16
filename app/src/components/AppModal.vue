<template>
    <div v-if="modalVisibility">
        <ion-backdrop></ion-backdrop>
        <div class="modal">
            <div class="modal__content">
                <img
                    style="align-self: end; position: absolute;"
                    src="../theme/images/close-outline.svg"
                    width="20"
                    @click="modalVisibility = false"
                />
                <div class="modal__text">
                    <slot />
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { IonSpinner, IonBackdrop, IonItemDivider } from '@ionic/vue';
import { ref, watch } from 'vue';

const emit = defineEmits(['update:model-value']);

const props = defineProps({
    modelValue: {
        type: Boolean,
        default: false
    },
});

const modalVisibility = ref(props.modelValue);

watch(() => props.modelValue, (newVal) => {
    modalVisibility.value = newVal;
});

watch(modalVisibility, (newVal) => {
    emit('update:model-value', newVal);
});

</script>

<style lang="scss" scoped>

ion-item-divider {
    font-size: 16px;
    line-height: 27px;
    color: #333333;
    padding-bottom: 10px;
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
    font-weight: 600;

    &__header {
        width: 100%;
        display: flex;
        justify-content: space-between;
    }

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
        color: #3A3A3A;
        font-weight: normal;
        max-height: calc(100vh - 200px);
        overflow-y: scroll;
        margin-top: -10px;
    }
}


</style>
