<template>
    <ion-header class="ion-no-border">
        <ion-toolbar>
            <ion-buttons slot="start">
                <ion-back-button
                    :icon="chevronBackOutline"
                    :default-href="backRoute"
                />
            </ion-buttons>
            <ion-title>
                {{ title }}
            </ion-title>
        </ion-toolbar>
    </ion-header>
</template>

<script setup>
import { IonHeader, IonTitle, IonToolbar, IonButtons, IonBackButton } from '@ionic/vue';
import { chevronBackOutline } from 'ionicons/icons';

defineProps({
    title: {
        type: String,
        required: true,
        default: 'App Title',
    },

    backRoute: {
        type: String,
        default: '/auth/login',
    },
});

</script>

<style lang="scss" scoped>

ion-icon {
    color: #4E4029;
}

ion-title {
    font-size: 18px;
    font-weight: 700;
    line-height: 25.2px;
    --color: #4E4029;
}
ion-toolbar {
    --background: #FFC660;
    --border-color: transparent;
}

</style>
