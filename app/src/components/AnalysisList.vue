<template>
    <div>
        <!-- <ion-searchbar
            v-model="search"
            placeholder="Buscar por nome da análise"
        /> -->
        <div
            v-if="!(filteredAnalytics.length === 0 && search)"
            class="analysis-list__count-label"
        >
            {{ analysisCountLabel }}
        </div>
        <div v-if="filteredAnalytics.length === 0">
            <empty-state
                title="Nenhuma análise encontrada"
                subtitle="Não foi encontrado nenhuma análise com base em sua busca, tente novamente"
                :image="NotFoundEmptyImage"
                margin-top="40px"
            />
        </div>
        <div
            v-else
            class="analysis-list"
        >
            <analysis-card
                v-for="(analysis, index) in filteredAnalytics"
                class="analysis-list__analysis-card"
                :analysis="analysis"
                :key="index"
                @on-card-click="$emit('on-card-click', $event);"
            />
        </div>
    </div>
</template>

<script setup>
import EmptyState from './EmptyState.vue';
import NotFoundEmptyImage from '../theme/images/not-found-empty.svg';
import AnalysisCard from './AnalysisCard.vue';
import { computed, ref, watchEffect } from 'vue';
import { IonSearchbar } from '@ionic/vue';

defineEmits(['on-card-click']);

const props = defineProps({
    analytics: {
        type: Array,
        default: () => ([]),
    }, 
});

const search = ref(null);
const filteredAnalytics = ref(props.analytics);

const analysisCountLabel = computed(() => {
    const listLength = filteredAnalytics.value.length;

    if (listLength === 1) {
        return `1 análise listada`;
    }

    if (listLength > 1) {
        return `${listLength} análises listadas`;
    }

    return 'Nenhuma análise listada';
});


const filterAnalyticsByName = () => {
    const searchValueLowerCase = search.value.toLowerCase();

    filteredAnalytics.value = props.analytics.filter(
        ({ name }) => name.toLowerCase().includes(searchValueLowerCase)
    );
};

watchEffect(() => {
    if (search.value) {
        filterAnalyticsByName();
    }
});

</script>

<style lang="scss" scoped>
.analysis-list {
    display: flex;
    flex-direction: column;
    gap: 12px;
    margin-top: 20px;

    &__count-label {
        margin-top: 20px;
        font-size: 14px;
        font-weight: 600;
        line-height: 16.94px;
        color: #474747;
    }

    &__schedule-card {
        margin-top: 24px;
        margin-bottom: 12px;
    }

    &__filter {
        margin-top: 24px;
    }
}

ion-searchbar {
    margin-top: 16px;
    --box-shadow: none;
    --placeholder-color: #ADADAD;
    --placeholder-font-weight: 400;
    --color: #6B6B6B;
    --icon-color: #ADADAD;
    --clear-button-color: #ADADAD;
    border-radius: 12px;
    padding: 5px 1px !important;
    border: 1px solid #E6E6E6;
}

:deep(.searchbar-input) {
    font-size: 14px !important;
}

</style>
