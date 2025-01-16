// sessionStorage.ts
import { getItem, setItem, removeItem, clearStorage } from './storageHelpers';

export const getSessionStorageItem = (key: string): string | null => getItem(sessionStorage, key);

export const setSessionStorageItem = (key: string, value: string): void => setItem(sessionStorage, key, value);

export const removeSessionStorageItem = (key: string): void => removeItem(sessionStorage, key);

export const clearSessionStorage = (): void => clearStorage(sessionStorage);
