import { createSlice } from '@reduxjs/toolkit';

import { getProgrammes } from './programmes.api';

const initialState = {
    searchQuery: '',
    ui: {
        isLoading: false,
        isLoaded: false,
        error: null,
    },
    results: [],
};

const { reducer, actions } = createSlice({
    name: 'programmes',
    initialState,
    reducers: {
        setSearchQuery: (state, { payload }) => {
            state.searchQuery = payload;
        },

        clearSearchQuery: (state) => {
            state.searchQuery = initialState.searchQuery;
            state.results = initialState.results;
        },

        loadResultsStart: (state) => {
            state.ui = { ...initialState.ui };
            state.ui.isLoading = true;
        },

        loadResultsSuccess: (state, { payload }) => {
            state.ui = { ...initialState.ui };
            state.ui.isLoaded = true;
            state.results = payload;
        },

        loadResultsError: (state, { payload }) => {
            state.ui = { ...initialState.ui };
            state.ui.error = payload;
        },
    },
});

export const { setSearchQuery, clearSearchQuery } = actions;

export const searchProgrammes = (searchQuery) => {
    return (dispatch) => {
        dispatch(actions.loadResultsStart());

        getProgrammes({
            query: searchQuery,
        }).then(
            (programmes) => {
                dispatch(actions.loadResultsSuccess(programmes));
            },
            (error) => {
                // If the API call was cancelled, we can safely dismiss that error.
                if (error.name !== 'AbortError') {
                    dispatch(actions.loadResultsError(error));
                }
            },
        );
    };
};

export default reducer;
