import { Storage } from '@ionic/storage';
import StorageORM from './StorageORM';

export default class Analisys extends StorageORM {
    static storage = new Storage({ name: 'analyses' });
};
