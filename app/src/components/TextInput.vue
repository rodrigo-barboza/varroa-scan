<template>
    <div>
        <label class="input__label">
            {{ label }}
        </label>
        <ion-input
            v-model="model"
            class="custom-input"
            type="number"
        >
        </ion-input>
        <small
			v-if="errorState"
			class="error-message"
		>
			{{ errorMessage }}
		</small>
    </div>
</template>

<script setup>
import { IonInput } from '@ionic/vue';
import { computed } from 'vue';

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


</script>

<style lang="scss" scoped>

.error-message {
    color: #ef4444;
    font-size: 12px;
};

.input {
    &__label {
        color: rgb(47, 47, 47);
        font-size: 14px;
        font-weight: 500;
        line-height: 21px;
    }
}

.custom-input {
    text-align: center;
    --border-color: rgba(149, 149, 149, 1);
    --highlight-color-focused: #ccc;
    --highlight-color-invalid: #dc3545;
    --background: rgba(250, 250, 250, 1);
    --border-width: 0px;
    border-bottom: 0px solid rgba(149, 149, 149, 1);

    input {
        border: none;
        border-top-left-radius: 0px;
        border-top-right-radius: 0px;
    }
}

</style>
