import { postAnalysis } from '../services/Analysis';
import { useAnalysisStore } from '../../store/analysesStore';
import Analisys from '../storage/Analisys';

export default class AnalysisController {
    constructor() {
        this.storage = Analisys;
    }

    async index() {
        return await this.storage.get();
    }

    async store(payload) {
        return await postAnalysis(payload);
    }

    async show(id) {
        const store = useAnalysisStore();
        store.isFetching = true;
        return await this.storage.find(id);
    }

    async save(analysis) {
        analysis.id = Math.floor(Math.random() * 1000000000) + 1;
        await this.storage.save(analysis);
        await this.reloadStore(); 
    }

    async delete(id) {
        await this.storage.remove(id);
        await this.reloadStore();        
    }

    async reloadStore() {
        const store = useAnalysisStore();
        await store.fetchAnalytics();
        store.isFetching = false;
    }
};
