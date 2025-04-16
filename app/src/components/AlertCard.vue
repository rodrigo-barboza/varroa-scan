<template>
    <div class="alert-card">
        <slot />
        <img :src="AlertIcon">
    </div>
</template>

<script setup>
import AlertIcon from '../theme/images/alert-icon.svg';
</script>

<style lang="scss" scoped>
.alert-card {
    padding: 4px 12px;
    gap: 0px;
    border-radius: 7px;
    border: 1px solid #FFDEDE;
    background: rgba(195, 41, 41, 0.06);
    color: rgba(201, 34, 34, 1);
    display: flex;
    justify-content: space-between;
    font-size: 12px;
    font-weight: 400;
    line-height: 20px;
    letter-spacing: -0.0001em;
}

</style>