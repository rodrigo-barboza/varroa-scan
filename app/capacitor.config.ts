import type { CapacitorConfig } from '@capacitor/cli';

const config: CapacitorConfig = {
	appId: 'br.com.varroascan.app',
	appName: 'Varroa Scan',
	webDir: 'dist',
	backgroundColor: '#f4fffb',
	plugins: {
		SplashScreen: {
			launchShowDuration: 3000,
			launchAutoHide: true,
			backgroundColor: "#ffffffff",
			androidSplashResourceName: "splash",
			androidScaleType: "CENTER_CROP",
			showSpinner: false,
			splashFullScreen: true,
			splashImmersive: true
		}
	}
};

export default config;
