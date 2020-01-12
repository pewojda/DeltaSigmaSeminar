function y=quant(x,B)
    Q=(1-(-1))/(2^B);
    y=floor(x/Q)*Q;
    %if y>=1 y=1; end
    %if y<-1 y=-1; end
end