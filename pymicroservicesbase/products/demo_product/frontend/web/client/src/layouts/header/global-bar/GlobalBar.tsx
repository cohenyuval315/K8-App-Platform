// "use client"

import LogoWithName from "@/components/common/logo/LogoWithName";
import GlobalBarEnd from "./GlobalBarEnd";
import GlobalBarStart from "./GlobalBarStart";
import UserNavigationMenu from "./components/user/UserNavigationMenu";
import AppHeaderSearch from "./components/search/AppHeaderSearch";





const GlobalBar = () => {
    return (
        <div
            className="AppHeader-globalBar"
            style={{
                display:"flex",

            }}>
                <GlobalBarStart>
                    <LogoWithName/>
                    <div></div>
                </GlobalBarStart>
                <GlobalBarEnd>
                    <AppHeaderSearch/>
                    <UserNavigationMenu/>
                </GlobalBarEnd>
        </div>
    );
};

export default GlobalBar;
