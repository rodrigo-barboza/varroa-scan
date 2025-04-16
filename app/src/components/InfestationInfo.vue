<template>
    <div class="infestation-info" :class="levelClass">
        <div class="metrics">
            <div class="metric-item">
                <span class="metric-value">{{ imagesAnalyzed }}</span>
                <span class="metric-label">Imagens analisadas</span>
            </div>
            <div class="metric-item">
                <span class="metric-value">{{ mitesCount }}</span>
                <span class="metric-label">Ácaros identificados</span>
            </div>
            <div class="metric-item">
                <span class="metric-value">{{ infestationLevelPercent }}%</span>
                <span class="metric-label">Nível de infestação</span>
            </div>
        </div>
    </div>
</template>

<script setup>

import { computed } from 'vue';

const props = defineProps({
    imagesAnalyzed: {
        type: Number,
        default: 0
    },
    mitesCount: {
        type: Number,
        default: 0
    },
    infestationLevel: {
        type: Number,
        default: 0
    }
});

const infestationLevelPercent = computed(() => {
    return parseFloat(props.infestationLevel).toFixed(2);
});

</script>

<style scoped>

.metrics {
    display: flex;
    justify-content: space-around;
    margin: 1.5rem 0;
    padding: 0.8rem;
    background-color: rgba(255, 255, 255, 0.7);
    border-radius: 12px;
    gap: 0.5rem;
}

.metric-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    flex: 1;
}

.metric-value {
    font-size: 1.2rem;
    font-weight: 700;
    color: #333;
}

.metric-label {
    font-size: 0.7rem;
    color: #666;
    text-align: center;
    margin-top: 0.3rem;
    line-height: 1.2;
}

/* Ajuste no espaçamento do "Saiba mais" */
.more-info {
    margin-top: 0.5rem;
}
</style>
