function plot_spec(x)
  f_len=length(x);
  sampl=length(x);
  half=f_len/2+1;
  freq=linspace(0,sampl/2+1,half);
  
  in_fft=fft(x/f_len,f_len);
  mag=abs(in_fft);
  mag=mag(1:half);
  db_mag=20*log10(mag);
  plot(freq,db_mag)
  grid on;
  ylim([-120,0])
  xlim([0,sampl/2+1])
  xlabel('Hz')
  ylabel('dB')