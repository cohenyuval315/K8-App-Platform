// store/store.js
import { configureStore } from '@reduxjs/toolkit';
import themeReducer from './features/theme/themeSlice';
import thunk from 'redux-thunk';
import { logger } from 'redux-logger';
import reduxMiddlewares from './middleware';
import reduxEnhancers from './enchanters';

export const makeStore = (preloadedState = {}) => {
    return configureStore({
        reducer: {
            theme: themeReducer,
        },
        devTools: process.env.NODE_ENV !== 'production',
        middleware: (getDefaultMiddleware) =>
            getDefaultMiddleware({
                actionCreatorCheck:false,
                immutableCheck:false,
                serializableCheck:false,
                thunk:{
                    extraArgument:undefined,
                },

            }).concat(logger, ...reduxMiddlewares),
        preloadedState,
        enhancers: (getDefaultEnhancers) =>
            getDefaultEnhancers().concat(...reduxEnhancers),
    });
};


// Infer the type of makeStore
export type AppStore = ReturnType<typeof makeStore>
// Infer the `RootState` and `AppDispatch` types from the store itself
export type RootState = ReturnType<AppStore['getState']>
export type AppDispatch = AppStore['dispatch']
