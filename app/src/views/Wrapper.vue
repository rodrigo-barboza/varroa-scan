<template>
    <ion-page id="main-content">
        <ion-content>
            <analysis class="view-container" />
            <main-menu active-tab="analysis" />
        </ion-content>
    </ion-page>
</template>

<script setup>
import Analysis from './Analysis.vue';
import MainMenu from '../components/Layout/MainMenu.vue';
</script>
