// localStorage.ts
import { getItem, setItem, removeItem, clearStorage } from './storageHelpers';

export const getLocalStorageItem = (key: string): string | null => getItem(localStorage, key);

export const setLocalStorageItem = (key: string, value: string): void => setItem(localStorage, key, value);

export const removeLocalStorageItem = (key: string): void => removeItem(localStorage, key);

export const clearLocalStorage = (): void => clearStorage(localStorage);
