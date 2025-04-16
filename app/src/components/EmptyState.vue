<template>
    <div class="container">
        <img :src="image" />
        <div class="title">
            {{ title }}
        </div>
        <div class="subtitle">
            {{ subtitle }}
        </div>
    </div>
</template>
  
<script setup>
import { computed } from 'vue';

const props = defineProps({
    image: {
        type: String,
        default: '',
    },

    title: {
        type: String,
        default: 'Ops, página não encontrada',
    },

    subtitle: {
        type: String,
        default: 'Se isso for um erro entre em contato com o suporte',
    },

    marginTop: {
        type: String,
        default: '150px',
    },
});

const resolveMarginTop = computed(() => props.marginTop);

</script>
  
<style scoped>
.container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin-top: v-bind(resolveMarginTop);
}

.title {
    margin-top: 1.15rem;
    font-size: 1.25rem;
    font-weight: 600;
    color: #414141;
    max-width: 80%;
    text-align: center;
}

.subtitle {
    margin-top: 0.5rem;
    margin-bottom: 1.5rem;
    width: 80%;
    font-size: 0.875rem;
    text-align: center;
    color: #5F5F5F;
}

</style>
