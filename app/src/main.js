import { createApp } from 'vue'
import App from './App.vue'
import router from './router';

import { IonicVue } from '@ionic/vue';
import { IonPage, IonContent } from '@ionic/vue';
import { SplashScreen } from '@capacitor/splash-screen';

import '@ionic/vue/css/core.css';
import '@ionic/vue/css/normalize.css';
import '@ionic/vue/css/structure.css';
import '@ionic/vue/css/typography.css';
import '@ionic/vue/css/padding.css';
import '@ionic/vue/css/float-elements.css';
import '@ionic/vue/css/text-alignment.css';
import '@ionic/vue/css/text-transformation.css';
import '@ionic/vue/css/flex-utils.css';
import '@ionic/vue/css/display.css';

import AnalisysStorage from './server/storage/Analisys';

import './theme/variables.css';

import { createPinia } from 'pinia';

const pinia = createPinia();

const app = createApp(App)
	.use(IonicVue)
	.use(router)
	.use(pinia);

app.component('IonPage', IonPage);
app.component('IonContent', IonContent);

AnalisysStorage.create();

router.isReady().then(() => {
	app.mount('#app');
	SplashScreen.show();
	setTimeout(() => {
		SplashScreen.hide();
	}, 3000);
});
