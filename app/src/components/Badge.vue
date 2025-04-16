<template>
    <div class="badge">
        <slot />
    </div>
</template>

<script setup>
import { computed } from 'vue';

const variantColorsMap = {
    success: {
        background: '#E2FFE1',
        color: '#4D9A4C',
    },
    info: {
        background: '#E0F2FF',
        color: '#5584A7',
    },
    warning: {
        background: '#FFF4E4',
        color: '#DD9F67',
    },
    danger: {
        background: '#FFE8E8',
        color: '#B55454',
    },
};

const props = defineProps({
    variant: {
        type: String,
        default: 'success',
        validate: (value) =>['success', 'warning', 'danger', 'info'].includes(value),
    },
});

const resolveBackgroundColor = computed(() => variantColorsMap[props.variant].background);
const resolveTextColor = computed(() => variantColorsMap[props.variant].color);

</script>

<style lang="scss" scoped>
.badge {
    background: v-bind(resolveBackgroundColor);
    color: v-bind(resolveTextColor);
    border-radius: 8px;
    padding: 4px 10px;
    width: fit-content;
    font-size: 14px;
    font-weight: 500;
    line-height: 21px;
}

</style>