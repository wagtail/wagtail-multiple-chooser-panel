import $ from 'jquery';

import { InlinePanel } from './InlinePanel';

class MultipleChooserPanel extends InlinePanel {
    constructor(opts) {
        super(opts);

        const chooserWidgetFactory = window.telepath.unpack(
            JSON.parse(document.getElementById(`${ opts.formsetPrefix }-CHOOSER_WIDGET`).textContent)
        );
        $(`#${ opts.formsetPrefix }-OPEN_MODAL`).on('click', () => {
            chooserWidgetFactory.openModal(
                (result) => {
                    result.forEach(item => {
                        this.addForm();
                    });
                },
                {multiple: true}
            );
        });
    }
}

window.MultipleChooserPanel = MultipleChooserPanel;
