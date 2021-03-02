import React from 'react';
import { NavBar } from './navigation/bar/bar';
import { useHistory } from 'react-router-dom';

export default function MainLayout(props: any) {
  let history = useHistory();

  function navigation(path: string) {
    history.push(path);
  }

  return (
    <div className="app">
      <header className="primary-header"></header>
      <aside className="primary-aside"></aside>
      <main>
        <NavBar navigation={navigation}></NavBar>
        {props.children}
      </main>
    </div>
  );
}
