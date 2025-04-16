import Env from '../helpers/env';

export const postAnalysis = (payload) => fetch(`${Env.API_URL}/api/v1/predict`, {
    method: 'POST',
    body: payload,
});
