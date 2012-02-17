$(function(){

  window.Post = Backbone.Model.extend({
      defaults: function(){
          return {
              created_on: new Date()
          };
      }
  });

  window.Blog = Backbone.Model.extend({});

  window.PostList = Backbone.Collection.extend({
      model: Post,
      localStorage: new Store("posts")

  });

  window.Posts = new PostList();

  window.PostView = Backbone.View.extend({
    tagName: 'li',
    template: _.template($('#post-template').html()),

    events: {
      "dblclick div.post-body": "edit",
      "keypress .post-input": "updateOnEnter"
    },

    initialize: function(){
      this.model.bind('change', this.render, this);
    },

    render: function(){
      var date = dateFormat(this.model.get('created_on'), 'm/dd/yy');
      $(this.el).html(this.template({
        date: date
      }));
      this.setText();
      return this;
    },

    setText: function(){
      var text = this.model.get('text');
      this.$('.post-body').text(text);
      this.input = this.$('.post-input');
      //this.input.bind('blur', _.bind(this.close, this)).val(text);
    },


    edit: function(){
      $(this.el).addClass("editing");
      this.input.focus();
    },


    updateOnEnter: function(e){
      if (e.keyCode == 13) this.close();
    }
  });

  window.AppView = Backbone.View.extend({
    el: $("#blogapp"),
    statsTemplate: _.template($("#stats-template").html()),
     events: {
       "keypress #new-post": "createOnEnter",
       "keyup #new-post": "showTooltip"
     },

    initialize: function(){
      this.input = this.$('#new-post');
      Posts.bind('add', this.addOne, this);
      Posts.bind('reset', this.addAll, this);
      Posts.bind('all', this.render, this);

      Posts.fetch();
    },

    render: function(){
      this.$('#post-stats').html(this.statsTemplate({
        total: Posts.length
      }));
    },

    addOne: function(post){
      var view = new PostView({model: post});
      $("#post-list").append(view.render().el);
    },

    addAll: function(){
      Posts.each(this.addOne);
    },

    createOnEnter: function(e) {
      var text = this.input.val();
      if (!text || e.keyCode != 13) return;
      Posts.create({text: text});
      this.input.val('');
    },


    showTooltip: function(e) {
      var tooltip = this.$(".ui-tooltip-top");
      var val = this.input.val();
      tooltip.fadeOut();
      if (this.tooltipTimeout) clearTimeout(this.tooltipTimeout);
      if (val === '' || val == this.input.attr('placeholder')) return;
      var show = function(){ tooltip.show().fadeIn(); };
      this.tooltipTimeout = _.delay(show, 1000);
    }
  });

  window.App = new AppView();
});
