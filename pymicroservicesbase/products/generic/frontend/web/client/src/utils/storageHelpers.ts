// shared/storageHelpers.ts

export const getItem = (storage: Storage, key: string): string | null => {
    if (typeof storage === 'undefined') return null;
    return storage.getItem(key);
};

export const setItem = (storage: Storage, key: string, value: string): void => {
    if (typeof storage === 'undefined') return;
    storage.setItem(key, value);
};

export const removeItem = (storage: Storage, key: string): void => {
    if (typeof storage === 'undefined') return;
    storage.removeItem(key);
};

export const clearStorage = (storage: Storage): void => {
    if (typeof storage === 'undefined') return;
    storage.clear();
};
