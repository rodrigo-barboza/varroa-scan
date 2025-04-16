<template>
    <app-modal v-model="model" title="Recomendações e tratamentos" width="600px">
        <div class="treatment-container">
            <div class="section">
                <h3 class="section-title">
                    <i class="icon-recommendations"></i>
                    Medidas Recomendadas
                </h3>
                <ul class="recommendation-list">
                    <li v-for="(item, index) in modalInfo.recommendations" :key="'rec-' + index"
                        class="recommendation-item">
                        <span class="bullet">•</span>
                        {{ item }}
                    </li>
                </ul>
            </div>
            <div v-if="modalInfo.treatments.length > 0" class="section">
                <h3 class="section-title">
                    <i class="icon-treatment"></i>
                    Protocolos de Tratamento
                </h3>
                <div class="treatment-grid">
                    <div v-for="(item, index) in modalInfo.treatments" :key="'treat-' + index" class="treatment-card">
                        <div class="treatment-name">{{ item.name }}</div>
                        <div class="treatment-method">
                            <span class="method-label">Método:</span>
                            {{ item.method }}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </app-modal>
</template>

<script setup>
import AppModal from './AppModal.vue';

const model = defineModel({
    type: Boolean,
    required: true,
});

defineProps({
    modalInfo: {
        type: Object,
        required: true
    }
});

</script>

<style lang="scss" scoped>
.section {
    margin-bottom: 1.5rem;
}

.section-title {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    color: #1f2937;
    font-size: .9rem;
    margin-bottom: .8rem;
    padding-bottom: 0.1rem;
}

.recommendation-list {
    list-style: none;
    padding: 0;
    margin: 0;
}

.recommendation-item {
    display: flex;
    gap: 0.5rem;
    font-size: 14px;
    padding: 0.5rem 0;
    line-height: 1.5;
    color: #4b5563;
}

.bullet {
    color: #3b82f6;
    font-weight: bold;
}

.treatment-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 1rem;
}

.treatment-card {
    background: #f9fafb;
    border-radius: 8px;
    padding: 1rem;
    border-left: 4px solid #3b82f6;
}

.treatment-name {
    font-weight: 600;
    color: #1f2937;
    margin-bottom: 0.25rem;
    font-size: .9rem;
}

.treatment-method {
    font-size: 0.8rem;
    color: #6b7280;
}

.method-label {
    font-weight: 500;
    color: #4b5563;
}

.emergency-note {
    background: #fef2f2;
    color: #b91c1c;
    padding: 0.75rem;
    border-radius: 6px;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.5rem;
    margin-top: 1rem;
    font-size: 0.9rem;
}
</style>