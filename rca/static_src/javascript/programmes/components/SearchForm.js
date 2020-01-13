import React, { useCallback } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import debounce from 'lodash.debounce';

import {
    setSearchQuery,
    clearSearchQuery,
    searchProgrammes,
} from '../programmes.slice';

import Icon from './Icon/Icon';
import { pushState, getIndexURL } from '../programmes.routes';

/**
 * A search form for programmes, visually only appearing as a single field.
 */
const SearchForm = ({
    searchQuery,
    label,
    setQuery,
    clearQuery,
    startSearch,
    isLoaded,
}) => {
    const startSearchDebounced = useCallback(debounce(startSearch, 300), [
        startSearch,
    ]);
    const showClearButton = searchQuery !== '' && isLoaded;

    return (
        <form
            onSubmit={(e) => {
                e.preventDefault();
                // Users can submit the search at any time even with no characters entered.
                startSearch(searchQuery);
            }}
            className="bg bg--dark"
            method="get"
            role="search"
        >
            <div className="grid">
                <div className="search search--programmes">
                    <label
                        className="search__label"
                        htmlFor="programmes-search-input"
                    >
                        {label}
                    </label>
                    <input
                        className="search__input input"
                        id="programmes-search-input"
                        type="search"
                        placeholder={label}
                        value={searchQuery}
                        onChange={(e) => {
                            const query = e.target.value;

                            setQuery(query);

                            if (query.length >= 3) {
                                startSearchDebounced(query);
                            }
                        }}
                    />
                    {showClearButton ? (
                        <button
                            className="search__button button body body--two"
                            type="button"
                            onClick={(e) => {
                                pushState(getIndexURL(), e);
                                clearQuery();
                            }}
                        >
                            Clear
                        </button>
                    ) : (
                        <button
                            className="search__button button"
                            type="submit"
                            aria-label="Search"
                        >
                            <Icon name="arrow" className="search__icon" />
                        </button>
                    )}
                </div>
            </div>
        </form>
    );
};

SearchForm.propTypes = {
    label: PropTypes.string,
    searchQuery: PropTypes.string.isRequired,
    isLoaded: PropTypes.bool.isRequired,
    setQuery: PropTypes.func.isRequired,
    clearQuery: PropTypes.func.isRequired,
    startSearch: PropTypes.func.isRequired,
};

SearchForm.defaultProps = {
    label: null,
};

const mapStateToProps = ({ programmes }) => {
    return {
        searchQuery: programmes.searchQuery,
        isLoaded: programmes.ui.isLoaded,
    };
};

const mapDispatchToProps = {
    setQuery: setSearchQuery,
    clearQuery: clearSearchQuery,
    startSearch: searchProgrammes,
};

export default connect(mapStateToProps, mapDispatchToProps)(SearchForm);