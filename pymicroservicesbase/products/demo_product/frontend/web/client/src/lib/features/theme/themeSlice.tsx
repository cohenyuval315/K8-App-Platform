import { createSlice } from '@reduxjs/toolkit';

const initialState = {
    mode: 'light', // or 'dark'
};

const themeSlice = createSlice({
    name: 'theme',
    initialState,
    reducers: {
        toggleTheme(state) {
            state.mode = state.mode === 'light' ? 'dark' : 'light';
        },
        setTheme(state, action) {
            state.mode = action.payload;
        },
    },
});

export const { toggleTheme, setTheme } = themeSlice.actions;
export const selectTheme = (state: { theme: { mode: any; }; }) => state.theme.mode;
export default themeSlice.reducer;
