<template>
    <ion-page>
        <ion-content>
            <div class="view-container">
                <app-title
                    title="Resultado da análise"
                    subtitle="Verifique abaixo o resultado da análise das imagens enviadas"
                />
                <spinner v-if="store.isFetching" />
                <template v-else>
                    <infestation-level-badge
                        :level="results.infestationLevel"
                        @show-more="handleShowModal"
                    />
                    <infestation-info
                        :images-analyzed="results.analizedImages"
                        :mites-count="results.varroaDetectedCount"
                        :infestation-level="results.infestationPercent"
                    />
                    <div
                        v-if="store.currentAnalysis.labeledImages.length > 0"
                        class="analysis-header"
                    >
                        <p class="subtitle">
                            Verifique abaixo o resultado da análise das imagens enviadas
                        </p>
                    </div>
                    <div
                        v-for="(image, index) in store.currentAnalysis.labeledImages" :key="index"
                        class="analysis-result-image"
                    >
                        <img :src="image">
                    </div>
                </template>
            </div>
        </ion-content>
        <show-details-modal
            v-model="showDetailsModal"
            :modal-info="modalInfo"
        />
        <details-botton-actions
            @back="handleBackRouter"
            @delete="handleDeleteResult"
            @save="handleSaveResult"
        />
    </ion-page>
</template>

<script setup>
import { onIonViewDidEnter } from '@ionic/vue';
import { computed, ref } from 'vue';
import { useAnalysisStore } from '../store/analysesStore';
import { useRoute, useRouter } from 'vue-router';
import AnalysisController from '../server/controllers/AnalysisController';
import AppTitle from '../components/Layout/AppTitle.vue';
import DetailsBottonActions from '../components/DetailsBottonActions.vue';
import InfestationInfo from '../components/InfestationInfo.vue';
import InfestationLevelBadge from '../components/InfestationLevelBadge.vue';
import ShowDetailsModal from '../components/ShowDetailsModal.vue';
import Spinner from '../components/Spinner.vue';

const route = useRoute();
const router = useRouter();
const store = useAnalysisStore();
const showDetailsModal = ref(false);
const modalInfo = ref(null);

const results = computed(() => store.currentAnalysis.results);

const fetchAnalytics = async () => {
    const { id } = route.params;

    if (id) {
        store.currentAnalysis  = await (new AnalysisController).show(id);
    }

    setTimeout(() => store.isFetching = false, 100);
};

const handleBackRouter = () => router.back();
const handleShowModal = (currentModalInfo) => (modalInfo.value = currentModalInfo, showDetailsModal.value = true);

const handleSaveResult = () => {
    store.isFetching = true;
    (new AnalysisController()).save(store.currentAnalysis);
    router.push({ name: 'home' });
};

const handleDeleteResult = () => {
    store.isFetching = true;
    (new AnalysisController()).delete(store.currentAnalysis.id);
    router.push({ name: 'home' });
};

onIonViewDidEnter(() => fetchAnalytics());

</script>

<style lang="scss" scoped>
.task {
    &__badges {
        display: flex;
        gap: 8px;
        margin-bottom: 12px;
    }

    &__schedule-card {
        margin-top: 16px;
    }
}

.analysis-result {
    margin-top: 24px;
    font-size: 16px;
    font-weight: 600;
    color: #525252;
    display: flex;
    flex-direction: column;
    gap: 1px;
    margin-bottom: 24px;
}

.analysis-result-image {
    border: 2px dashed #9C9C9C;
    border-radius: 12px;
    padding: 6px;
    margin-bottom: 12px;
}

img {
    border-radius: 12px;
}

.analysis-header {
    text-align: center;
    margin-bottom: 1.5rem;
    padding: 0 1rem;
}

.subtitle {
    font-size: 0.95rem;
    color: #6b7280;
    margin-bottom: 1rem;
}

.recommendations {
    font-size: 12px;
    padding: 0px 16px;
    display: flex;
    flex-direction: column;
    gap: 8px;
}

h4 {
    margin-top: 0px;
    padding: 0px;
    font-size: 14px;
}

</style>
