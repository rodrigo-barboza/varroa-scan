import { createRouter, createWebHistory } from '@ionic/vue-router';
import AnalysisResult from '../views/AnalysisResult.vue';
import NewAnalisys from '../views/NewAnalisys.vue';
import Wrapper from '../views/Wrapper.vue';

const routes = [
	{
		path: '/',
		redirect: { name: 'home' },
	},
	{
		path: '/home',
		name: 'home',
		component: Wrapper,
	},
	{
		path: '/analysis/:id?',
		name: 'analysis.result',
		component: AnalysisResult,
	},
	{
		path: '/new-analysis',
		name: 'new-analysis',
		component: NewAnalisys,
	},
];

const router = createRouter({
	history: createWebHistory(import.meta.env.BASE_URL),
	routes,
});

export default router;
