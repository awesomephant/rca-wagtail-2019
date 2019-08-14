import '@babel/polyfill';

import Menu from './components/menu';
import SubMenu from './components/submenu';
import BackLink from './components/back-link';
import MobileSubMenu from './components/mobile-sub-menu';
import CookieWarning from './components/cookie-message';
import Accordion from './components/accordion';
import Carousel from './components/carousel';
import Slideshow from './components/slideshow';
import ProgressBar from './components/progress-bar';
import VideoModal from './components/video-modal';
import RelatedContent from './components/related-content';
import Tabs from './components/tabs';
import Sticky from './components/position-sticky-event';
import './components/sticky-header';

import '../sass/main.scss';

document.addEventListener('DOMContentLoaded', function() {
    const cookie = document.querySelector(CookieWarning.selector());
    new CookieWarning(cookie);

    for (const accordion of document.querySelectorAll(Accordion.selector())) {
        new Accordion(accordion);
    }

    for (const carousel of document.querySelectorAll(Carousel.selector())) {
        new Carousel(carousel);
    }

    for (const slideshow of document.querySelectorAll(Slideshow.selector())) {
        new Slideshow(slideshow);
    }

    for (const menu of document.querySelectorAll(Menu.selector())) {
        new Menu(menu);
    }

    for (const backlink of document.querySelectorAll(BackLink.selector())) {
        new BackLink(backlink);
    }

    for (const submenu of document.querySelectorAll(SubMenu.selector())) {
        new SubMenu(submenu);
    }

    for (const relatedcontent of document.querySelectorAll(
        RelatedContent.selector(),
    )) {
        new RelatedContent(relatedcontent);
    }

    for (const mobilesubmenu of document.querySelectorAll(
        MobileSubMenu.selector(),
    )) {
        new MobileSubMenu(mobilesubmenu);
    }

    // Toggle subnav visibility
    for (const subnavBack of document.querySelectorAll('[data-subnav-back]')) {
        subnavBack.addEventListener('click', () => {
            subnavBack.parentNode.classList.remove('is-visible');
        });
    }

    for (const progressbar of document.querySelectorAll(
        ProgressBar.selector(),
    )) {
        new ProgressBar(progressbar);
    }

    for (const videomodal of document.querySelectorAll(VideoModal.selector())) {
        new VideoModal(videomodal);
    }

    for (const tabs of document.querySelectorAll(Tabs.selector())) {
        new Tabs(tabs);
    }

    for (const sticky of document.querySelectorAll(Sticky.selector())) {
        new Sticky(sticky);
    }
});
