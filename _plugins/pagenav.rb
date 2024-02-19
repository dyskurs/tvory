module Jekyll

    module NextPrevId
  
      def next(id)
        orderlist = @context.registers[:site].data["order"]
        ind = orderlist.index(id)
        if ind
          return orderlist[ind+1]
        else
          return nil
        end
      end
  
      def prev(id)
        orderlist = @context.registers[:site].data["order"]
        ind = orderlist.index(id)
        if ind
          return orderlist[ind-1]
        else
          return nil
        end
      end
  
    end
  
  end
  
  Liquid::Template.register_filter(Jekyll::NextPrevId)