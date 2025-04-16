<template>
    <div class="schedules-filter">
        <filter-button
            v-for="{ key, name } in filters"
            :key="key"
            :active="activeFilter === key"
            @click="activeFilter = key"
        >
            {{ name }}
        </filter-button>
    </div>
</template>

<script setup>
import { ref, watch } from 'vue';
import FilterButton from './FilterButton.vue';

const emit = defineEmits(['on-filter-change']);

const filters = [
    {
        key: 1,
        name: 'Ver todas',
        active: true,
    },
    {
        key: 2,
        name: 'As que sou responsável',
        active: false,
    },
    {
        key: 3,
        name: 'Tarefas para hoje',
        active: false,
    },
];

const activeFilter = ref(1);

watch(activeFilter, (key) => {
    filters.forEach(item => {
        item.active = item.key === key;
    });

    emit('on-filter-change', key);
});

</script>

<style lang="scss" scoped>
.schedules-filter {
    display: flex;
    gap: 8px 4px;
    flex-wrap: wrap;
}
</style>