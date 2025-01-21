"use client"

import SearchInput from "@/components/general/input/SearchInput";
import { ChangeEvent, useState } from "react";

const AppHeaderSearch = () => {
    const [searchInput,setSearchInput] = useState("");

    const onSearchInputChange = (e: ChangeEvent<HTMLInputElement>) => {
        setSearchInput(e.target.value);
    }

    return (
        <SearchInput
            onChange={onSearchInputChange}
            value={searchInput}
            className="AppHeader-search"
            placeholder=""
        />
    )
}

export default AppHeaderSearch;
