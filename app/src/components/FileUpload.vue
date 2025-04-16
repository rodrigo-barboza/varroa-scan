<template>
    <div class="file-button">
		<div class="file-button__content">
			<div class="file-button__main">
				<img :src="resolveIcon">
				<div class="file-button__text">{{ resolveButtonText }}</div>
			</div>
			<img
				v-if="hasDocument"
				class="file-button__close-button"
				:src="CloseIcon"
				@click.stop="emit('remove-file', item)"
			>
		</div>
    </div>
</template>

<script setup>
import UploadIcon from '../theme/images/upload.svg';
import DocumentIcon from '../theme/images/document.svg';
import CloseIcon from '../theme/images/close-outline.svg';
import { computed } from 'vue'

const emit = defineEmits(['remove-file']);

const props = defineProps({
	item: {
		type: String,
		required: true,
		default: null,
	},
});

const resolveFileName = computed(() => {
	if (props.item?.webPath) {
		return `${props.item.webPath.split('/').pop()}.${props.item.format}`;
	}
	
	return props.item?.name;
});
const hasDocument = computed(() => props.item);
const resolveButtonText = computed(() => hasDocument.value ? resolveFileName.value : 'Carregar imagem');
const resolveIcon = computed(() => hasDocument.value ? DocumentIcon : UploadIcon);
const resolveTextAlignment = computed(() => hasDocument.value ? 'space-between' : 'center');

</script>
<style lang="scss" scoped>

.file-button {
	font-size: 13.5px;
	font-weight: 470;
	border: 2px dashed #DFE5EC;
	border-radius: 12px;
	padding: 24px 14px;
	height: 40px;
	display: flex;
	justify-content: center;
	align-items: center;
	cursor: pointer;
	width: 100%;

	&__main {
		display: flex;
		justify-content: center;
		align-items: center;
		gap: 8px;
	}

	&__content {
		display: flex;
		justify-content: space-between;
		align-items: center;
		gap: 8px;
		width: 100%;
	}

	&__close-button {
		height: 24px;
		width: 24px;
		cursor: pointer;
	}

	&__text {
		width: 200px;
		white-space: nowrap;
		overflow: hidden;
		text-overflow: ellipsis;
	}
}
</style>