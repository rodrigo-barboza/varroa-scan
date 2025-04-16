<template>
    <div
        class="filter-button"
        :class="{ 'filter-button--active': active }"
    >
        <div class="filter-button__content">
            <slot></slot>
            <img
                v-if="active"
                :src="CheckIcon"
            />
        </div>
    </div>
</template>

<script setup>
import CheckIcon from '../theme/images/check.svg';

defineProps({
    active: {
        type: Boolean,
        default: false,
    },
});

</script>

<style lang="scss" scoped>

.filter-button {
    padding: 6px 12px;
    border-radius: 30px;
    border: 1px solid rgb(230, 230, 230);
    font-size: 14px;
    font-weight: 400;
    line-height: 19.6px;
    color: rgb(133, 133, 133);
    width: fit-content;

    &__content {
        display: flex;
        gap: 5px;

        img {
            align-self: center;
            width: 15px;
            height: 13.5px;
        }
    }

    &--active {
        color: rgb(138, 100, 41);
        background: rgba(255, 180, 46, 1);
    }
}

</style>
