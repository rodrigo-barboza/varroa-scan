export const snakeToCamelCase = (str) => {
    str = (str === '_id') ? 'id' : str;
    return str.replace(/(_\w)/g, match => match[1].toUpperCase());
}

export const camelToSnakeCase = (str) => {
    return str.replace(/[A-Z]/g, match => `_${match.toLowerCase()}`);
}

export const convertKeysToCamelCase = (obj) => {
    if (Array.isArray(obj)) {
        return obj.map(convertKeysToCamelCase);
    } else if (obj !== null && obj.constructor === Object) {
        const newObj = {};
        Object.keys(obj).forEach(key => {
            const newKey = snakeToCamelCase(key);
            newObj[newKey] = convertKeysToCamelCase(obj[key]);
        });
        return newObj;
    }

    return obj;
}

export const convertKeysToSnakeCase = (obj) => {
    if (Array.isArray(obj)) {
        return obj.map(convertKeysToSnakeCase);
    } else if (obj !== null && obj.constructor === Object) {
        const newObj = {};
        Object.keys(obj).forEach(key => {
            const newKey = camelToSnakeCase(key);
            newObj[newKey] = convertKeysToSnakeCase(obj[key]);
        });
        return newObj;
    }

    return obj;
}