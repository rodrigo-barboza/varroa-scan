<template>
    <div style="margin-top: 12px;">
        <label class="input__label">
            {{ label }}
        </label>
        <div
            class="number-input"
            :class="errorState ? 'number-input--invalid' : ''"
        >
            <div
                class="number-input__signals number-input__signals--border-right"
                @click="decrementValue"
            >
                -
            </div>
            <div class="number-input__value">
                <text-input v-model="model" />
            </div>
            <div
                class="number-input__signals number-input__signals--border-left"
                @click="incrementValue"
            >
                +
            </div>
        </div>
        <small
			v-if="errorState"
			class="error-message"
		>
			{{ errorMessage }}
		</small>
    </div>
</template>

<script setup>
import { computed } from 'vue';
import TextInput from './TextInput.vue';

const model = defineModel({
    type: Number,
    default: 0,
});

const props = defineProps({
    label: {
        type: String,
        default: '',
    },

    state: {
        type: String,
        default: '',
    },

    errorMessage: {
        type: String,
        default: '',
    },
});

const errorState = computed(() => props.state == 'invalid');

const incrementValue = () => model.value++;
const decrementValue = () => {
    if (model.value > 0) {
        model.value--;
    }
};

</script>

<style lang="scss" scoped>

.error-message {
    color: #ef4444;
    font-size: 12px;
};

.input {
    &__label {
        margin-top: 24px;
        color: rgb(47, 47, 47);
        font-size: 14px;
        font-weight: 500;
        line-height: 21px;
    }
}

.number-input {
    margin-top: 11px;
    border-radius: 12px;
    border: 1px solid #DFE5EC;
    background: rgb(252, 252, 252);
    display: flex;
    justify-content: space-between;
    overflow: hidden;
    color: rgb(0, 0, 0);
    font-size: 16px;
    font-weight: 500;
    line-height: 24px;

    &--invalid {
        border: 1px solid #ef4444;
    }

    &__value {
        min-width: 200px;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    &__signals {
        background: rgb(246, 246, 246);
        width: 100%;
        height: 100%;
        padding: 12px;
        display: flex;
        justify-content: center;
        align-items: center;
        cursor: pointer;
        
        &--border-left {
            border-left: 1px solid #DFE5EC;
        }

        &--border-right {
            border-right: 1px solid #DFE5EC;
        }
    }
}

</style>