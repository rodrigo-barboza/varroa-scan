<template>
	<div class="menu">
		<ion-button
			class="menu__add"
			shape="round"
			@click="handleRedirectTo('new-analysis')"
		>
			<img src="../../theme/images/plus.svg">
		</ion-button>
	</div>
</template>
<script>
import { IonButton } from '@ionic/vue';

export default {
	components: {
		IonButton,
	},

	props: {
		activeTab: {
			type: String,
			default: 'analysis',
		},
	},

	data() {
		return {
			currentTab: this.activeTab,
		};
	},

	watch: {
		activeTab(activeTab) {
			this.currentTab = activeTab;
		},
	},

	methods: {
		isActive(tab) {
			return this.currentTab === tab;
		},

		handleTabClick(tab) {
			this.currentTab = tab;
			this.$emit('on-tab-changed', tab);
		},

		handleRedirectTo(route) {
			this.$router.push({ name: route });
		},
	},
};
</script>

<style lang="scss" scoped>
@import "../../theme/css/main-menu.scss";

.menu__add {
	position: absolute;
	left: calc(50%);
	top: 1px;
	transform: translate(-50%, -50%);
	width: 64px;
	height: 64px;

    --background: #FFA41B;
	--border-radius: 50%;
	--box-shadow: 0px 8px 8px 0px #f3c888;
}

img {
	max-width: 19px;
}

.side {
    display: flex;
    justify-content: space-around;
    gap: 12px;
}

.menu {
	position: fixed;
	bottom: 0;
    margin-bottom: 0px;
	display: flex;
	justify-content: space-between;
    padding-inline: 20px;
	align-items: center;
	width: 100%;
	height: 50px;

	@include menu-background;
}

.active {
	--box-shadow: none;
	--background: #ddb373;
	--border-radius: 30px;
    filter: invert(5%) sepia(6500%) saturate(150%) hue-rotate(-5deg) brightness(102%) contrast(104%);
}
</style>
