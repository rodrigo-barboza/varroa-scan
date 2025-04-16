import { convertKeysToCamelCase } from '../helpers/snakeCaseConvert';

export default class StorageORM {
    static storage = null;

    static async create() {
		await this.storage.create();
	}

    static async saveMany(items) {
        const savePromises = items.map((item) => convertKeysToCamelCase(item))
            .map((item) => this.storage.set(item.id, item));

        await Promise.all(savePromises);
    }

    static async save(item) {
        await this.storage.set(item.id, convertKeysToCamelCase(item));
    }

    static async find(id) {
        return await this.storage.get(id);
    }

    static async get() {
        const ids = await this.storage.keys();

        const itemsPromise = ids.map((id) => this.storage.get(id));

        return await Promise.all(itemsPromise);
    }

    static async size() {
        return await this.storage.length();
    }

    static async removeAll() {
        await this.storage.clear();
    }

    static async remove(id) {
        await this.storage.remove(id);
    }
}
