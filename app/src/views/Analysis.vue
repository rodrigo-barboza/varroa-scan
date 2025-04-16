<template>
   <div>
        <app-title
            title="Histórico de análises"
            subtitle="Visualize todas as análises feitas"
            with-menu
        />
        <spinner v-if="store.isFetching" />
        <template v-else>
            <empty-state
                v-if="store.getAnalytics?.length === 0"
                title="Nenhuma análise realizada"
                subtitle="Você ainda não realizou nenhuma análise, clique no
                botão inferior para realizar sua primeira análise"
                :image="AnalysisEmptyImage"
            />
            <analysis-list
                v-else
                :analytics="store.getAnalytics"
                @on-card-click="redirectToAnalysisDetails"
            />
        </template>
   </div>
</template>

<script setup>
import { useAnalysisStore } from '../store/analysesStore';
import { useRouter } from 'vue-router';
import AnalysisList from '../components/AnalysisList.vue';
import AnalysisEmptyImage from '../theme/images/apiaries-empty.svg';
import AppTitle from '../components/Layout/AppTitle.vue';
import EmptyState from '../components/EmptyState.vue';
import Spinner from '../components/Spinner.vue';

const router = useRouter();
const store = useAnalysisStore();

const redirectToAnalysisDetails = (id) => {
    store.isFetching = true;
    router.push({ name: 'analysis.result', params: { id }});
};

store.fetchAnalytics();

setTimeout(() => store.isFetching = false, 100);

</script>
