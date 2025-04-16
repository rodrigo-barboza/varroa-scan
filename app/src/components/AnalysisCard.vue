<template>
    <div>
        <div class="analysis-card">
            <div
                class="analysis-card__badges"
                v-if="!noBadge"
            >
                <badge variant="info">Análise</badge>
                <badge :variant="resolveAnalysisVariant?.variant">
                    {{ resolveAnalysisVariant?.name }}
                </badge>
            </div>
            <div class="analysis-card__title">
                Nível de infestação: {{ analysis.results.infestationPercent ? parseFloat(analysis.results.infestationPercent).toFixed(2) : '0' }}%
            </div>
            <div class="analysis-card__time">
                <img :src="ClockImage">
                <div>{{ analisysDate }}</div>
            </div>
            <div class="analysis-card__analized_images_count">
                Número de imagens analisadas: {{ analysis.results.analizedImages }}
            </div>
            <button
                v-if="!hiddenButton"
                class="analysis-card__button"
                @click="$emit('on-card-click', analysis.id)"
            >
                {{ buttonText }}
            </button>
        </div>
    </div>
</template>

<script setup>
import { computed } from 'vue';
import { STATUS } from '../constants/analysisLevel';
import Badge from './Badge.vue';
import ClockImage from '../theme/images/clock.svg';

const props = defineProps({
    analysis: {
        type: Object,
        default: () => ({}),
        required: true,
    },

    buttonText: {
        type: String,
        default: 'Ver detalhes',
    },

    hiddenButton: {
        type: Boolean,
        default: false,
    },
});

const resolveAnalysisVariant = computed(() =>  {
    return STATUS[props.analysis.results.infestationLevel] ?? STATUS[0]
});

const analisysDate = computed(() => props.analysis.analizedAt
    ? Intl.DateTimeFormat('pt-BR').format(new Date(props.analysis.analizedAt * 1000))
    : '-'
);

</script>

<style lang="scss" scoped>
.analysis-card {
    padding: 20px 16px;
    border-radius: 17px;
    border: 1px solid rgba(230, 230, 230, 1);
    display: flex;
    flex-direction: column;
    gap: 12px;

    &__badges {
        display: flex;
        gap: 8px;
    }

    &__title {
        font-size: 16px;
        font-weight: 600;
        line-height: 24px;
        color: rgba(82, 82, 82, 1);
    }

    &__time {
        font-size: 14px;
        font-weight: 500;
        line-height: 21px;
        color: rgba(80, 80, 80, 1);
        display: flex;
        gap: 4px;
    }

    &__analized_images_count {
        margin-top: 4px;
        display: flex;
        gap: 2px;
        font-size: 14px;
        font-weight: 500;
        line-height: 21px;
        color: rgba(123, 123, 123, 1);
    }

    &__button {
        padding: 12px 20px;
        gap: 4px;
        border-radius: 8px;
        border: 1px solid rgb(255, 235, 205);
        background: rgb(255, 235, 205);
        color: rgba(139, 89, 1, 1);
        font-weight: 600;
        font-size: 14px;
        line-height: 21px;

        &:hover {
            cursor: pointer;
            background: rgb(255, 239, 205)
        }
    }
}

</style>
