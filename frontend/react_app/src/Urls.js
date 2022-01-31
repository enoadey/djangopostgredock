import React from "react";
import { BrowserRouter, Route,  Routes, Navigate } from "react-router-dom";

import SignIn from "./components/Login";
import Home from "./components/Home";
import PasswordUpdate from "./components/PasswordUpdate";

// A wrapper for <Route> that redirects to the login screen if you're not yet authenticated.
function PrivateRoute({ isAuthenticated, children, ...rest}) {
    return (
      <Route
        {...rest}
        render={({ location }) =>
        isAuthenticated ? (
            children
          ) : (
            <Navigate
              to={{
                pathname: "/login/",
                state: { from: location }
              }}
            />
          )
        }
      />
    );
  }

function Urls(props) {

    return (
        <div>
            <BrowserRouter>
                < Routes>
                    <Route exact path="/login/" element={<SignIn />} />
                    <Route exact path="/update_password/" isAuthenticated={props.isAuthenticated} element={<PrivateRoute/>} element={<PasswordUpdate/>}/>
                    <Route exact path='/' element={<Home/>}/>
                </ Routes>
            </BrowserRouter>
        </div>
    )
};

export default Urls;