frappe.ui.form.ControlData = frappe.ui.form.ControlData.$extend({
    make_input: function(){
        var options = this.df.options;
        if (!options || options!=="Translatable"){
            this._super();
            return;
        }
        var me = this;
        $('<div class="link-field" style="position: relative;">\
            <input class="input-with-feedback form-control" type="text"/>\
            <span class="dialog-btn">\
                <a class="btn-open no-decoration" open="" title="\
                __(">\
                <i class="fa fa-globe"></i>\
                </a>\
            </span>\
        </div>').prependTo(this.input_area);
        this.$input_area = $(this.input_area);


        this.$input = this.$input_area.find('input');
        this.$btn = this.$input_area.find('.dialog-btn');
        this.set_input_attributes();
        this.$input.on("focus", function(){
            me.$btn.toggle(true);
        });
        this.$input.on("blur", function(){
            setTimeout(function(){ me.$btn.toggle(false) }, 500);
        });
        this.input = $this.input.get(0);
        this.has_input = true;
        var me = this;
        this.setup_button();
    },
    setup_button: function(){
        var me = this;
        if (this.only_input){
            this.$btn.remove();
            return;
        }
        this.$btn.on("click", function(){
            var value = me.get_value();
            var options = me.df.options;
            if (value && options && options==="Translatable"){
                this.open_dialog();
            }
        });
    },
    open_dialog: function(){
        if (this.frm && !this.frm.is_dirty()) {
            new frappe.ui.form.TranslationSelector({
                doc: doc,
                df: this.doc,
                text: this.value
            });
        }
    }
});
