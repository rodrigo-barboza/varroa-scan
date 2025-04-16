<template>
    <div class="new-analisys">
        <div class="new-analisys__actions">
            <button
                class="new-analisys__secondary-button"
                @click="emit('back')"
            >
                <
            </button>
            <button
                v-if="route.params.id"
                class="new-analisys__button"
                @click="emit('delete')"
            >
                Excluir análise
            </button>
            <button
                v-else
                class="new-analisys__button"
                @click="emit('save')"
            >
                Salvar resultado
            </button>
        </div>
    </div>
</template>

<script setup>
import { useRoute } from 'vue-router';

const route = useRoute();

const emit = defineEmits(['back', 'save', 'delete']);

</script>

<style lang="scss" scoped>
.new-analisys {
    background: #fff;
    width: 100%;
    height: 80px;

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
