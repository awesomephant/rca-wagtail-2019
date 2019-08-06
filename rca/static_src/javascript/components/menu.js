class Menu {
    static selector() {
        return '[data-menu-toggle]';
    }

    constructor(node) {
        this.node = node;
        this.body = document.querySelector('body');
        this.closeIcon = document.querySelector('[data-close-menu]');
        this.drawerOpenClass = 'nav-open';
        this.menuOpenClass = 'menu-active';
        this.searchOpenClass = 'search-active';
        this.activeClass = `${this.node.dataset.active}-active`;
        this.bindEventListeners();
    }

    bindEventListeners() {
        this.node.addEventListener('click', (e) => {
            e.preventDefault();
            this.toggle();
        });

        this.closeIcon.addEventListener('click', (e) => {
            e.preventDefault();
            this.close();
        });
    }

    toggle() {
        // if the drawer is open
        if(this.body.classList.contains(this.drawerOpenClass)) {
            // and search is clicked
            if((this.node.dataset.active === 'search')) {
                // and the search is active
                if(this.body.classList.contains(this.searchOpenClass)){
                    // close the drawer
                    this.close();
                } else {
                    // activate the search
                    this.body.classList.remove(this.menuOpenClass);
                    this.body.classList.add(this.searchOpenClass);
                }
            // and menu is clicked
            } else if (this.node.dataset.active === 'menu') {
                // and the menu is active
                if(this.body.classList.contains(this.menuOpenClass)){
                    // close the drawer
                    this.close();
                } else {
                    // activate the menu
                    this.body.classList.remove(this.searchOpenClass);
                    this.body.classList.add(this.menuOpenClass);
                }
            }
        } else {
            // open the drawer
            this.open();
        }
    }

    open() {
        this.body.classList.add(this.drawerOpenClass, this.activeClass);
    }

    close() {
        this.body.classList.remove(this.drawerOpenClass, this.activeClass);
    }
}

export default Menu;
