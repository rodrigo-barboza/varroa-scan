<template>
    <div class="infestation-info" :class="levelClass">
        <div class="header">
            <span class="level">
                {{ label }}
            </span>
            <h3 class="title">{{ title }}</h3>
        </div>
        <p class="description">{{ description }}</p>
        <span class="more-info" @click="handleEmitShowMore">Saiba mais</span>
    </div>
</template>

<script setup>
import { computed } from 'vue'

const emit = defineEmits(['show-more'])

const props = defineProps({
    level: {
        type: String,
        required: true,
        validator: value => ['healthy', 'low', 'medium', 'high'].includes(value),
    }
})

const label = computed(() => ({
    high: 'Alta',
    medium: 'Média',
    low: 'Baixa',
    healthy: 'Saudável'
}[props.level]))

const title = computed(() => ({
    high: 'Infestação Alta',
    medium: 'Infestação Moderada',
    low: 'Infestação Leve',
    healthy: 'Sem Infestação'
}[props.level]))

const description = computed(() => ({
    high: 'Foi detectada uma infestação severa. Ações imediatas são recomendadas.',
    medium: 'Há sinais consideráveis de infestação. Recomenda-se intervenção.',
    low: 'Pequenos sinais foram encontrados. Continue monitorando.',
    healthy: 'Nenhum ácaro foi identificado nas imagens analisadas.',
}[props.level]));

const infestationLevels = [
    {
        level: "healthy",
        recommendations: [
            "Manter monitoramento mensal (cheque-alveolar ou método de lavagem com álcool)",
            "Continuar boas práticas de manejo preventivo",
            "Inspecionar colmeias vizinhas pois podem ser fonte de reinfestação"
        ],
        treatments: [],
        emergency: false,
    },
    {
        level: "low",
        recommendations: [
            "Aplicar tratamentos orgânicos como ácido oxálico ou fórmico em doses baixas",
            "Manejar quadros de cria para reduzir células disponíveis",
            "Instalar telas excluidoras de fundo"
        ],
        treatments: [
            { name: "Ácido oxálico", method: "gotejamento ou sublimação" },
            { name: "Ácido fórmico", method: "65% em aplicadores tipo MiteAway™" }
        ],
        emergency: false,
    },
    {
        level: "medium",
        recommendations: [
            "Aplicar tratamento combinado com ácido fórmico e timol",
            "Remover 2-3 quadros de cria operculada (método de quebra de ciclo)",
            "Fornecer alimentação estimulante para fortalecer colônia",
            "Considerar isolamento da colmeia em casos >30%"
        ],
        treatments: [
            { name: "Ácido fórmico", method: "85% em método Nassenheider" },
            { name: "Timol", method: "Apiguard® após 14 dias" }
        ],
        emergency: true,
    },
    {
        level: "high",
        recommendations: [
            "Aplicar tratamento emergencial com sublimação de ácido oxálico + amitraz",
            "Eliminação total da cria (método de sacrifício de quadros)",
            "Confinamento da rainha por 21 dias (quebra do ciclo reprodutivo)",
            "Em casos >70%: considerar união com colônia forte ou eliminação da colmeia"
        ],
        treatments: [
            { name: "Ácido oxálico", method: "Sublimação" },
            { name: "Amitraz", method: "Apivar® simultaneamente" }
        ],
        emergency: true,
    }
];

const levelClass = computed(() => `level-${props.level}`);

const handleEmitShowMore = () => {
    const levelInfo = infestationLevels.find(level => level.level === props.level);
    emit('show-more', levelInfo);
}

</script>

<style scoped>
.infestation-info {
    padding: 1rem;
    border-radius: 16px;
    /* Borda arredondada mais suave */
    background-color: #f9fafb;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
    /* Sombra suave */
    margin: 1rem;
    font-family: 'Arial', sans-serif;
}

.header {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: 1rem;
}

.level {
    font-size: 0.85rem;
    font-weight: 700;
    padding: 0.4rem 0.8rem;
    border-radius: 50px;
    /* Estilo pill para a badge */
    color: #fff;
    background-color: #aaa;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin-bottom: 0.5rem;
    text-transform: uppercase;
}

.level-icon {
    font-size: 1.1rem;
}

.title {
    font-size: 1.2rem;
    font-weight: 600;
    margin: 0;
    color: #333;
    text-align: center;
}

.description {
    font-size: 0.9rem;
    color: #555;
    margin: 0.4rem 0 0.8rem;
    text-align: center;
}

.more-info {
    font-size: 0.85rem;
    color: #1d4ed8;
    text-decoration: none;
    cursor: pointer;
    transition: color 0.3s ease, transform 0.2s ease;
}

.more-info:hover {
    color: #2563eb;
    transform: scale(1.05);
}

/* Cores por nível */
.level-high .level {
    background-color: #ef4444;
    /* Vermelho */
}

.level-medium .level {
    background-color: #f59e0b;
    /* Laranja */
}

.level-low .level {
    background-color: #10b981;
    /* Verde */
}

.level-healthy .level {
    background-color: #3b82f6;
    /* Azul */
}
</style>
