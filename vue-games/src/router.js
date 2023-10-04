import { createWebHistory, createRouter  } from 'vue-router';

import AboutView from './views/AboutView.vue';
import AnagramHuntView from './views/AnagramHuntView.vue';
import HomeView from './views/HomeView.vue';
import MathFactsView from './views/MathFactsView.vue';

const routes = [
    {
        path: '/',
        name: 'HomeView',
        component: HomeView
    },
    {
        path: '/about',
        name: 'AboutView',
        component: AboutView
    },
    {
        path: '/games/anagram-hunt',
        name: 'AngramHuntView',
        component: AnagramHuntView
    },
    {
        path: '/games/math-facts',
        name: 'MathFactsView',
        component: MathFactsView
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes: routes,
});

export default router;