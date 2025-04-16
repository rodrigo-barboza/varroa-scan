import { defineStore } from 'pinia';
import { computed, ref } from 'vue';
import AnalysisController from '../server/controllers/AnalysisController';
import { convertKeysToCamelCase } from '../server/helpers/snakeCaseConvert';

export const useAnalysisStore = defineStore('analyses', () => {
    const currentAnalysis = ref({});
    const analytics = ref([]);
    const isFetching = ref(false);

    const getAnalytics = computed(() => analytics.value);

    const setCurrentAnalysis = (analysis) => currentAnalysis.value = convertKeysToCamelCase(analysis);

    const fetchAnalytics = async () => {
        isFetching.value = true;
        analytics.value = await (new AnalysisController).index();
    };

    return {
        isFetching,
        fetchAnalytics,
        setCurrentAnalysis,
        currentAnalysis,
        getAnalytics,
    };
});
