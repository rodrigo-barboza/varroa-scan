export const HEALTHY = 'healthy';
export const LOW = 'low';
export const MEDIUM = 'medium';
export const HIGH = 'high';

export const STATUS = {
	[HEALTHY]: { name: 'Sem ocorrência', variant: 'success' },
	[LOW]: { name: 'Baixo risco', variant: 'info' },
	[MEDIUM]: { name: 'Médio risco', variant: 'warning' },
	[HIGH]: { name: 'Alto risco', variant: 'danger' },
};

export const ALL_STATUS = [
	HEALTHY,
	LOW,
	MEDIUM,
	HIGH,
];
